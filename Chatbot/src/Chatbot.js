/**
 * Chatbot Component
 * 
 * This React component implements a simple chatbot interface that allows users to interact with a server-based AI 
 * by sending and receiving messages. The component maintains a list of messages exchanged between the user and 
 * the bot, and provides a text input for users to type their messages. Messages are sent to a backend server via 
 * a POST request, and the server's response is displayed in the chat window.
 * 
 * Key Features:
 * - Uses React's useState hook to manage the input text and the list of messages.
 * - Sends user messages to a server API endpoint (`/generate`) using the Fetch API.
 * - Displays server responses or error messages within the chat interface.
 * - Supports sending messages by pressing the "Enter" key or clicking the "Send" button.
 * 
 * Styling:
 * - The component is styled using inline CSS with a simple and clean design, ensuring a user-friendly interface.
 * - Different styles are applied to user and bot messages to distinguish between them visually.
 * 
 * Environment Variables:
 * - `REACT_APP_PORT`: The port number of the backend server is fetched from environment variables.
 * 
 * Usage:
 * - Include the Chatbot component in a React application to enable chatbot functionality.
 * - Ensure that a backend server is running and accessible at the specified port.
 * 
 * @component
 * @author Carlos L. Gray
 */


// src/Chatbot.js
import React, { useState } from 'react';

const Chatbot = () => {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);

    const sendMessage = async () => {
        if (input.trim() === '') return;

        const userMessage = { sender: 'user', text: input };
        setMessages(prevMessages => [...prevMessages, userMessage]);

        const port = process.env.REACT_APP_PORT || 5001; // Default to 5001 if REACT_APP_PORT isn't set

        try {
            const response = await fetch(`http://localhost:${port}/generate`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "query": input
                })
            });

            // Parse the response JSON
            const data = await response.json();

            if (response.ok) {
                const botMessage = { sender: 'bot', text: data.response }; // Use the response field
                setMessages(prevMessages => [...prevMessages, botMessage]);
            } else {
                const botMessage = { sender: 'bot', text: 'Error: Unable to fetch response.' };
                setMessages(prevMessages => [...prevMessages, botMessage]);
            }

        } catch (error) {
            console.error('Error communicating with the server:', error);
            const botMessage = { sender: 'bot', text: 'Error communicating with the server.' };
            setMessages(prevMessages => [...prevMessages, botMessage]);
        }

        setInput('');
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    };

    return (
        <div style={styles.container}>
            <div style={styles.chatWindow}>
                {messages.map((msg, index) => (
                    <div
                        key={index}
                        style={{
                            ...styles.message,
                            ...(msg.sender === 'user' ? styles.userMessage : styles.botMessage),
                        }}
                    >
                        {msg.text}
                    </div>
                ))}
            </div>
            <div style={styles.inputContainer}>
                <input
                    style={styles.input}
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder="Type your message..."
                />
                <button style={styles.button} onClick={sendMessage}>
                    Send
                </button>
            </div>
        </div>
    );
};

const styles = {
    container: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        backgroundColor: '#f4f4f4',
    },
    chatWindow: {
        width: '80%',
        height: '70%',
        overflowY: 'scroll',
        backgroundColor: '#fff',
        border: '1px solid #ddd',
        borderRadius: '5px',
        padding: '10px',
        marginBottom: '10px',
    },
    message: {
        padding: '10px',
        margin: '5px 0',
        borderRadius: '5px',
    },
    userMessage: {
        backgroundColor: '#dcf8c6',
        alignSelf: 'flex-end',
    },
    botMessage: {
        backgroundColor: '#ececec',
        alignSelf: 'flex-start',
    },
    inputContainer: {
        display: 'flex',
        width: '80%',
    },
    input: {
        flex: 1,
        padding: '10px',
        fontSize: '16px',
        borderRadius: '5px',
        border: '1px solid #ddd',
        marginRight: '10px',
    },
    button: {
        padding: '10px 20px',
        fontSize: '16px',
        borderRadius: '5px',
        border: 'none',
        backgroundColor: '#007bff',
        color: '#fff',
        cursor: 'pointer',
    },
};

export default Chatbot;

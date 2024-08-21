/**
 * App Component
 * 
 * This is the main entry point for the React application. The App component serves as a simple wrapper for 
 * rendering the Chatbot component. It is responsible for including the Chatbot within a basic container 
 * that could be further expanded with additional components or styling as needed.
 * 
 * Key Features:
 * - Renders the Chatbot component, providing a user interface for interacting with the chatbot.
 * - Acts as the root component of the React application, which can be extended to include more features.
 * 
 * Usage:
 * - Include additional components or layout elements within the App component to expand the application's functionality.
 * 
 * @component
 * @author Carlos L. Gray
 */


// src/App.js
import React from 'react';
import Chatbot from './Chatbot';

function App() {
    return (
        <div>
            <Chatbot />
        </div>
    );
}

export default App;

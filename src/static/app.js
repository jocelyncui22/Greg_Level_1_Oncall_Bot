document.addEventListener('DOMContentLoaded', () => {
    const messageForm = document.getElementById('messageForm');
    const messageInput = document.getElementById('messageInput');
    const messageArea = document.getElementById('messageArea');
    const messageTemplate = document.getElementById('messageTemplate');

    // Sample user data
    const currentUser = {
        id: 'U123456',
        name: 'You',
        isBot: false
    };

    function formatTimestamp(date) {
        return date.toLocaleTimeString('en-US', { 
            hour: '2-digit', 
            minute: '2-digit'
        });
    }

    function createMessageElement(message, isBot = false) {
        const messageElement = messageTemplate.content.cloneNode(true);
        const messageDiv = messageElement.querySelector('.message');
        
        messageDiv.classList.add(isBot ? 'bot-message' : 'user-message');
        
        const username = messageElement.querySelector('.username');
        username.textContent = isBot ? 'Greg Bot' : 'You';
        
        const timestamp = messageElement.querySelector('.timestamp');
        timestamp.textContent = formatTimestamp(new Date());
        
        const content = messageElement.querySelector('.message-content');
        
        // Handle markdown-style formatting
        let formattedMessage = message;
        
        // Convert code blocks
        formattedMessage = formattedMessage.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
        
        // Convert bold text
        formattedMessage = formattedMessage.replace(/\*(.*?)\*/g, '<strong>$1</strong>');
        
        content.innerHTML = formattedMessage;
        
        return messageElement;
    }

    async function sendMessage(text) {
        try {
            // Add user message to chat
            messageArea.appendChild(createMessageElement(text));
            
            // Scroll to bottom
            messageArea.scrollTop = messageArea.scrollHeight;
            
            // Send message to backend
            const response = await fetch('/api/message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user: currentUser.id,
                    text: text,
                    channel: 'help-data-eng'
                }),
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            
            // Add bot response to chat
            messageArea.appendChild(createMessageElement(data.response.text, true));
            
            // Scroll to bottom again
            messageArea.scrollTop = messageArea.scrollHeight;
            
        } catch (error) {
            console.error('Error:', error);
            messageArea.appendChild(createMessageElement('Sorry, I encountered an error processing your request.', true));
        }
    }

    messageForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const text = messageInput.value.trim();
        if (!text) return;
        
        messageInput.value = '';
        await sendMessage(text);
    });

    // Add some initial messages
    const welcomeMessage = `👋 Welcome to the Greg Bot Simulator! 

I'm here to help with:
- Snowflake queries and performance issues
- Code repository searches
- Deployment and pipeline problems

Try asking me something like:
- "My Snowflake query is running slow"
- "Can you help me find the main data pipeline code?"
- "I'm getting deployment errors in staging"`;

    messageArea.appendChild(createMessageElement(welcomeMessage, true));
});
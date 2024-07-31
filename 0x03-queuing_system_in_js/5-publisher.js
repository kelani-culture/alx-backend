import { createClient } from 'redis';

// Create a Redis client
const publisher = createClient();

// Listen for the connect event to confirm connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the error event to handle connection errors
publisher.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Publishes a message to the 'holberton school channel' after a delay
 * @param {string} message - The message to publish
 * @param {number} time - The delay in milliseconds before publishing the message
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send message: ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

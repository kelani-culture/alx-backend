import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Listen for the connect event to confirm connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the error event to handle connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to set a new school in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

// Function to display the value of a school from Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
}

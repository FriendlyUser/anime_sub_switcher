import { Storage } from 'npm:megajs'
import { config } from 'https://deno.land/x/dotenv@v3.2.2/mod.ts';

// Load environment variables from .env file if present
try {
  config({ export: true }); // export: true makes the variables accessible to the process env.
} catch (error) {
  console.warn("Couldn't load .env file, using existing environment variables.");
}

const email = Deno.env.get('MEGA_EMAIL');
const password = Deno.env.get('MEGA_PASSWORD');
const userAgent = Deno.env.get('MEGA_USER_AGENT') || 'Uploaded/1.0'; // Default user agent if not set.


if (!email || !password) {
  console.error('MEGA_EMAIL and MEGA_PASSWORD environment variables must be set.');
  Deno.exit(1); // Exit the script if required variables are missing
}

const storage = new Storage({
  email: email,
  password: password,
  userAgent: userAgent
})

console.log("Mega Storage initialized with environment variables.")


// Example Usage (Illustrative - replace with your actual code)
// You might want to wrap your storage logic in an async function.

async function main() {
  try {
    await storage.ready; // Ensure the storage is ready before using it
    console.log("Mega Storage is ready.");

    // Example: List the root folder content
    const files = await storage.root.children;
    console.log("Root folder contents:", files.map(file => file.name));


  } catch (error) {
    console.error("Error interacting with Mega:", error);
  }
}

main();
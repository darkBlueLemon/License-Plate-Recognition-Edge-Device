#!/bin/bash

# Function to handle cleanup on SIGINT
cleanup() {
    echo "Terminating all background processes..."
    pkill -P $$
    wait
    echo "All background processes terminated."
    exit 0
}

# Trap SIGINT (Ctrl+C) and call cleanup function
trap cleanup SIGINT

# Start the first script in the background
python3 app.py & 

# Start the second script in the background
python3 process_images.py &

# Start the third script in the background
python3 main.py &

# Wait for all background processes to finish
wait


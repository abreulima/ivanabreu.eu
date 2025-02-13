#!/bin/bash

# Names to scroll
names=("prondina" "jemoreir" "jdiniz-c")

# Scroll names
clear
for name in "${names[@]}"; do
    echo -n "$name "
    sleep 0.5  # Adjust speed of scrolling here
done
echo -e "\n"

# Thankful message
echo "🙏 Thank you for being amazing! 🙏"
sleep 1

# Scroll names again
for name in "${names[@]}"; do
    echo -n "$name "
    sleep 0.5
done
echo -e "\n"

# Another thankful message
echo "Grateful for each and every one of you! 🙌"
sleep 2

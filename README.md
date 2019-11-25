# Big Cheef's Suprise Mechanics by MAWD™

## Roles:                                </br>
Mohidul Abedin - Project Manager, Balance </br>
William Cao - Pokemon Game </br>
Devin Lin - Rick and Morty Game </br>
Alex Olteanu - To21 game </br>

## Description
Our website is a collection of top-tier, big-brain, and purely skill based games. Use our IN-GAME currency to play Pokemon Versus, to21 (not blackjack btw) and Rick and Morty trivia. You can also redeem your winnings from the games into your paypal account or (maybe) buy MICROTRANSACTIONS. 

## API and Frontend Framework
  - [PokeApi](https://docs.google.com/document/d/1hMbL36d5qqFLfufHOqUMWwraWFudfJdekqp6urex0KU/edit)
  - [Currency Exchange](https://docs.google.com/document/d/1yTckLoGBHA-C37hhukXOc76Jh_770L7m3Moj-wMFeUU/edit)
  - [Deck of Cards](https://docs.google.com/document/d/1oCJhl-NoNNpekMLd4C4jBXhpL9xvm6ZrVIdfoqbq-Vc/edit#heading=h.cx298swl620u)
  - [Rick and Morty](https://docs.google.com/document/d/1oK0klhp__LHP9kxb3D70cbbI46i1mMnmDMI4y1XS3B4/edit)
  - [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

## Instructions to Run
1. Open a terminal. Run the following lines in the terminal to clone the repository and change directory into it.
    ```bash
    git clone https://github.com/Mabedin00/MAWD.git && cd MAWD
    ```
2. Install python virtualenv if it has not been done so already.  
    ```bash
    # For macOS and Linux
    python3 -m pip install --user virtualenv
    # For Windows
    py -m pip install --user virtualenv
    ```
3. Initialize the server by running the following:
    ```bash
    ./init.sh
    ```
4. Activate the virtual environment by running the appropriate command:
    ```bash
    # If you are running zsh
    source venv/bin/activate
    # If you are running bash
    . venv/bin/activate
    ``` 
5. Start the web server by running:
    ```bash
    python3 app.py
    ```
6. Open a web browser and type the following into the address "127.0.0.1:5000"

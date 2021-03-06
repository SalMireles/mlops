## MLOps - Crypto Trading

Uses Flask to allow users to follow various cryptocurrency trends. Dash is integrated into the app as a seperate feature to run custom stock analysis and predictions.

![Dash Demo](https://github.com/SalMireles/mlops/blob/master/app/static/app-demo.jpg?raw=true)

 This project was started as a collaborative sprint between multiple developers and eventually I forked it to complete it and put a nice bow on it. See original PR history here: https://github.com/PDXPythonPirates/ppp-project-2
 
 Personal Goals: 
  - Learn the ins and outs of Flask for web app developement
  - Containerization using Docker
  - Schema design and working with Databases
  - Deploying and productionizing an app
  - Contiuous Integration
  - Extend the app to run stock analysis
<details open>
<summary>Tech Stack Information</summary>
<br>
   <ul>

<li> Flask Backend</li>
<li> Utilized github actions for continuous integration and testing</li>
<li> Containerized using docker compose</li>
<li> Javascript and Jinja frontend rendering</li>
<li> Integrated dash app for quick analysis</li>
<li> Utilizes CoinGecko API to gather coin data</li>
<li> Added MySQL database for prod deployment</li>
<li> pre-commit linting to adhere to black and flake8</li>
<li> Added unit tests to verify page functionality</li>

   </ul>
</details>

## How to boot the app

 **Note**: You need an .env file with credentials to boot the mysql container locally.

 <details>
<summary>Required environment variables</summary>
<br>
   <ul>

<li> DATABASE_URL</li>
<li> DB_USER</li>
<li> DB_PASSWORD</li>
<li> DB_HOST</li>
<li> DB_NAME</li>
<li> DB_PORT</li>
<li> DATABASE_URL_DOCKER</li>

   </ul>
</details>

<details>
<summary>Pre-configuration install Notes for Windows</summary>
<br>
   <ul>

<li> Install choclatey as an administrator (from powershell): https://chocolatey.org/install</li>
<li> Use choco to install make (also from the powershel as admin): `choco install make`</li>
<li> Install poetry. This can be a pain on Windowns. Use docker containers or another virtual environment.</li>
<li> Use WSL to execute make commands on windows. Alternatively, you can run the commands in the make file one by one.</li>

   </ul>
</details>

- #### With docker compose (recommended for prod)
    1. run `make up` 
       * Runs the docker containers locally and opens on  http://localhost:5000 (this also boots a mysql container)
    2. run `make down` 
       * Stops containers and prunes

- #### In your local environment (recommended for dev)
    1. run `make install` 
       * Installs dependencies and jump into the virtual env
    2. run `flask run` 
       * Boots the app locally. Make sure you are in the top level directory that has the file "app_run.py"


## Working with Docker
* Install Docker by following the instructions on [their site](https://docs.docker.com/get-docker/)
* run `make stop` to stop containers and prune

## Working with Poetry

* Install a new dep/library run `poetry add <your_dep>` or `poetry add <dep> --dev`
* Resolve poetry.lock files. Use 1. to resolve on github or 2. to resolve locally (recommended)
   1. On github **click** on resolve conflicts and follow [this guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github)
   2. Locally, pull the recent changes. Remove the lock file with the conflict `rm poetry.lock`. run `make install` to regenerate the lock file. Push changes and give yourself a high five!


## Enable Virtual Environment and Install Packages

### Mac

* Note: make sure poetry is installed and first time setup is complete
* Take a look at the Makefile to see what shell commands are being executed
   ```bash
   make install
   ```

## Adding Python Dependencies

0. we use [poetry](https://python-poetry.org/) to track python deps
0. to install a new dep run `poetry add <your_dep>` or `poetry add <dep> --dev`
0. you can also modify the pyproject.toml directly, then run `poetry lock --no-update`

## First-Time Setup

### Mac
* Install [brew](https://brew.sh/)
* Install pyenv
   ```bash
   brew install pyenv
   echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```
* Install [zsh](https://sourabhbajaj.com/mac-setup/iTerm/zsh.html)
   ```bash
   brew install zsh
   ```
* Install Python 3.8.10
   ```bash
   pyenv install 3.8.10
   ```

### Troubleshooting

Help with various installation/setup issues:

 * [Mac](#Mac)
https://github.com/culturerobotics/universe/blob/fbc0dd1da6ad3ea3da11001d0a9adfdddc7630a9/vessel/cookbook/cora075_scalable_process_5L.py#L320
#### Mac

- Error port 5000 already in use. How to free up this port: system preferences > sharing > uncheck airplay receiver.

## References
1. [Flask Mega Tutorial - by Miguel Grinberg - 2018](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Other References
1. Testing Markdown - [dillinger.io](https://dillinger.io/)

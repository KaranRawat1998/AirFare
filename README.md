
# Air Fare

Nowadays, airline ticket prices can vary dynamically for the same flight. Customers are seeking to get the lowest price while airlines are trying to keep their overall revenue as high as possible and maximize their profit. Airlines use various kinds of computational techniques to increase their revenue such as demand prediction and price discrimination. But from customer perspective they want to save money so i have proposed a model that predicts the approximate ticket price so that customer can find when is the optimal time to buy a ticket is. 

The Flight Fare Prediction predict the flight price using regression based Machine Learning algorithms and helps users look for optimal time and prices to book flight tickets.

# Table of contents
* [Air Fare](#air-fare)
* [Demo](#demo)
* [Table of contents](#table-of-contents)
* [Dataset](#dataset)
* [Installation](#installation)
* [Contributing](#contributing)
* [Deployment](#deployment)
* [Technologies Used](#technologies-used)

## Demo
[(Back to top)](#table-of-contents)

Heroku WebApp: https://flight-price-1.herokuapp.com/

[![](https://i.imgur.com/4VSHxE9.png?1)](https://flight-price-1.herokuapp.com/)

Database: https://flight-price-1.herokuapp.com/Database

[![](https://i.imgur.com/QWJNepK.png?1)](https://flight-price-1.herokuapp.com/Database)

AWS cloud : http://ec2-65-1-133-122.ap-south-1.compute.amazonaws.com:8080/

## Dataset
[(Back to top)](#table-of-contents)

 - [Dataset Link](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh)


## Installation
[(Back to top)](#table-of-contents)

create an environment with python version=3.7

```bash
    conda create -n yourenvname python=3.7
```
activating yourenvname
```bash
    activate yourenvname
```
cd to the directory where requirements.txt is located.
```bash
    C:\Users>cd where requirements.txt is located
```
install necessary libraries in yourenvname
```bash
    pip install -r requirements.txt
```
Now you are good to run the python scripts and ipynb files

## Contributing
[(Back to top)](#table-of-contents)

**Fork this repository**

Fork this repository by clicking on the fork button on the top of this page. This will create a copy of this repository in your account.
  
**Clone the repository**

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the copy to clipboard icon.

Open a terminal and run the following git command:
```bash
    git clone "url you just copied"
```
**Commit Changes to the branch**

Add those changes to the branch you just created using the `git add` command:
```bash
    git add file
```
Now commit those changes using the `git commit` command:
```bash
    git commit -m "string"
```
**Push changes to GitHub**

Push your changes using the command `git push`:
```bash
    git push origin <add-your-branch-name>
```
## Deployment
[(Back to top)](#table-of-contents)

To deploy this project on aws cloud

1. Create EC2 instance in aws.

2. Add security group for all traffic.

3. Download Putty And Puttygen and winscp.

4. Download .pem file after launching an ec2 instance.

5. Generate a private key file using Puttygen.
    
6. Connect winscp to ubuntu VPS and load private key file.

```bash
    by entering host name like this: ubuntu@ec2-**-*-***-***.ap-south-*.compute.amazonaws.com
```
7. Now drag and drop the required files into your ubuntu virtual private server.
    
8. Now Launch putty and load private key file and hostname and after entering putty session as soon as you login you enter the command prompt of ubuntu server.
    
9. Firstly we will update our pip by using commands like:
```bash
    sudo apt-get update && sudo apt-get install python3-pip
```
10. Now to install all the required libraries we will install requirements.txt
```bash
    pip3 install -r requirements.txt
```
11. Now before deploying your model into cloud you need to start `tmux` session to keep your processes running even after you close your ssh session.
 ```bash
    tmux
``` 
12. after Entering tmux session you need to host and deploy your model onto aws cloud.
```bash
    python3 flight.py
```
13. Now your model is accessible at your given port



  
## Technologies Used
[(Back to top)](#table-of-contents)

![](https://forthebadge.com/images/badges/made-with-python.svg)
[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) 
[<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) 
[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/)
[<img target="_blank" src="https://miro.medium.com/max/792/1*lJ32Bl-lHWmNMUSiSq17gQ.png" width=170>](https://developer.mozilla.org/en-US/docs/Web/HTML)
[<img target="_blank" src="https://prnewsjournal.com/wp-content/uploads/2020/11/aws-logo.png" width=170>](https://aws.amazon.com/)
[<img target="_blank" src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_bf0fb4cb7fe948c42f37ded73895638f/salesforce-heroku.png" width=170>](https://en.wikipedia.org/wiki/Heroku)
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Cassandra_logo.svg/1200px-Cassandra_logo.svg.png" width=170>](https://cassandra.apache.org/_/index.html)


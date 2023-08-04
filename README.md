# Pezesha

![Pezesha](./pezesha.png)

## Run with Docker Compose

This works if you have docker instlled 

Run services:
`docker-compose up -d --remove-orphans`

Bring services down:
`docker-compose down`

on Windows

Install python

Install requirements

Run the project

## Delployment

The docker image is deployed to the Image registry. You simply pull and run the image.

## Auth

![auth](./auth.png)

Go to this endpoint use username:pezesha password:pezesha 

![auth](./accesstoken.png)

Copy access token

![auth](./token.png)

Go to authorize and paste the token, the close.

## Create

![auth](./create.png)

Use this to create account.
`{
  "account_name": "test",
  "account_type": "current_account",
  "balance": "1000"
}`

## Send

![auth](./send.png)

`{
  "from_account": 2,  
  "to_account": 1,    
  "amount": 2000
}
`

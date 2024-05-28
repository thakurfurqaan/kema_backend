## Running Locally using Docker
- Run: `docker-compose up --build`
- Run (in new terminal T2): `docker exec -it kema_backend-web-1 /bin/bash`
- Run (in T2): `python manage.py migrate`
- Run (in T2): `python manage.py setup`


## Technical Future Scope
- Rate limits for creating payment requests.
- Send email / SMS notification to the client with the payment link using Sendgrid and Twilio.
- Pagination for the dropdowns

## NOTES
-  `.env` file has not been gitignored for the sake of the assignment.
- I usually use a service layer for medium to large scale apps for the business logic so that it could be reused over several interfaces and APIs.
- For payment gateway integrations, we can implement callback API endpoints to handle the final state of the payment request
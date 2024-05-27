## Running Locally using Docker
- Run: `docker-compose up --build`

## Initial Setup
- Launch Terminal: `docker exec -it kema_backend-web-1 /bin/bash`
- Run: `python manage.py setup`


## Technical Future Scope
- Rate limits for creating payment requests.
- Send email / SMS notification to the client with the payment link using Sendgrid and Twilio.
- Pagination for the dropdowns

## NOTES
-  `.env` file has not been gitignored for the sake of the assignment.
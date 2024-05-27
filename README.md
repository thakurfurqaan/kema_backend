## Running Locally using Docker
- Run: `docker-compose up --build`
- Run (in new terminal T2): `docker exec -it kema_backend-web-1 /bin/bash`
- Run (in T2): `python manage.py migrate`
- Run (in T2): `python manage.py setup`

## Initial Setup



## Technical Future Scope
- Rate limits for creating payment requests.
- Send email / SMS notification to the client with the payment link using Sendgrid and Twilio.
- Pagination for the dropdowns

## NOTES
-  `.env` file has not been gitignored for the sake of the assignment.
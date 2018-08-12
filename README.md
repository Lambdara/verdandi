# Verdandi

Verdandi is a program to make a daily schedule implemented in Flask, implementing a REST API.

## Specification

*Not fully implemented yet*

The default result is to retun a web page. If the `Accept` header is set to `application/json`, then it will return JSON instead.

- For `GET` and `DELETE` requests headers and body are ignored.
- For `POST` and `PATCH` the body/data of the request should contain JSON specifying the desired changes.

| Path                       | Description        | Modes              |
| -------------------------- | ------------------ | ------------------ |
| `/`                        | Web interface root | GET                |
| `/schedules/`              | List of schedules  | GET, POST, DELETE  |
| `/schedules/<SCHEDULE_ID>` | Schedule object    | GET, PATCH, DELETE |
| `/events/`                 | List of events     | GET, POST, DELETE  |
| `/events/<EVENT_ID>`       | Event object       | GET, PATCH, DELETE |

Schedule object:
```
{
  "id": <SCHEDULE_ID>, # Integer
  "name": <NAME>, # String, this is optional
  "date": <DATE>, # String, this is optional, format: YYYY-MM-DD
  "events": [<EVENT>,..] # List of event objects
}
```

Event object:
```
{
  "id": <EVENT_ID>, # Integer
  "name": <NAME>, # String
  "start_time": <DATE>, # String, this is optional, format: YYYY-MM-DD
  "end_time": <DATE>, # String, this is optional, format: YYYY-MM-DD
  "schedule_id": <SCHEDULE_ID> # Integer, referencing event object
}
```

## Dependencies

- Flask

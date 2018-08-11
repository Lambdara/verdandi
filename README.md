# Verdandi

Verdandi is a program to make a daily schedule

## Specification

/Not fully implemented yet/

Communication via JSON.

| Path                       | Description        | Modes              |
|----------------------------+--------------------+--------------------|
| `/`                        | Web interface      | GET                |
| `/schedules/`              | Index of schedules | GET, POST, DELETE  |
| `/schedules/<SCHEDULE_ID>` | Schedule object    | GET, PATCH, DELETE |
| `/events/`                 | Index of events    | GET, POST, DELETE  |
| `/events/<EVENT_ID>`       | Event object       | GET, PATCH, DELETE |

Schedule object:
```
{
  "id": <SCHEDULE_ID>, # Integer
  "name": <NAME>, # String, this is optional
  "date": <DATE>, # String, this is optional, format: YYYY-MM-DD
  "event_ids": [<EVENT_ID>,..] # List of integers, referencing event objects
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

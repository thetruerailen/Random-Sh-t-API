# Random Shit Archive API Documentation

The Random Shit Archive API allows you to retrieve the current time and set the time zone. This documentation provides information on how to use the API and the available endpoints.

## Base URL

We do not have a public URL yet, sorry!

## Endpoints

### 1. Get Current Time

- **Endpoint**: `/time`
- **Method**: `GET`
- **Description**: Retrieves the current time in the specified time zone.
----
- **Endpoint**: `/time/timezones`
- **Method**: `GET`
- **Description**: Retrieves the current time in the specified time zone.

#### Parameters

| Parameter  | Type   | Description                                     |
|------------|--------|-------------------------------------------------|
| `timezone` | string | (Optional) The time zone to retrieve the time.  |

#### Example

GET /time?timezone=America/New_York


##### Response

```json
{
  "time": "2023-05-19 12:30:00 EDT-0400"
}

GET /time/timezones

{
  "timezones": [
    "America/New_York",
    "America/Los_Angeles",
    "Europe/London",
    ...
  ]
}

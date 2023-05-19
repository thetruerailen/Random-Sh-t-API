from flask import Flask, request, jsonify
from datetime import datetime, timezone, timedelta
import pytz

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_time():
    # Get the requested time zone from the query parameters
    tz_name = request.args.get('timezone')
    
    # Set the default time zone to UTC
    tz = pytz.utc
    
    # If a valid time zone is provided, update the tz variable
    if tz_name:
        try:
            tz = pytz.timezone(tz_name)
        except pytz.exceptions.UnknownTimeZoneError:
            return jsonify({'error': 'Invalid time zone'}), 400
    
    # Get the current time in the specified time zone
    current_time = datetime.now(timezone.utc).astimezone(tz)
    
    # Format the time as a string
    time_str = current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Return the time as a JSON response
    return jsonify({'time': time_str})

@app.route('/time/timezones', methods=['GET'])
def get_timezones():
    # Get a list of all available time zones
    timezones = pytz.all_timezones
    
    # Return the list of time zones as a JSON response
    return jsonify({'timezones': timezones})

if __name__ == '__main__':
    app.run()

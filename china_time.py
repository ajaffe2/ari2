from datetime import datetime
import pytz

# Define the timezone for China
china_timezone = pytz.timezone('Asia/Shanghai')

# Get the current time in China
china_time = datetime.now(china_timezone)

# Print the current time in China
print("Current time in China:", china_time.strftime('%Y-%m-%d %H:%M:%S'))
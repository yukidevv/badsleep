from garminconnect import Garmin
from dotenv import load_dotenv
import os

def main():
  load_dotenv()
  client = Garmin()
  # client = Garmin(
  #   os.getenv("GARMIN_EMAIL"),
  #   os.getenv("GARMIN_PASSWORD"),
  # )
  client.login(".garminconnect")

  activities = client.get_activities(0, 10)
  for a in activities:
    print(a.get("activityName"), a.get("startTimeLocal"))

if __name__ == "__main__":
  main()

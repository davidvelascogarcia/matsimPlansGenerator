'''
  * ***************************************************************
  *      Program: MATSim Plans Generator
  *      Type: Python
  *      Author: David Velasco Garcia @davidvelascogarcia
  * ***************************************************************
'''

# Libraries
import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()

import argparse
import cv2
import datetime
from halo import Halo
import pandas as pd
import platform


class MATSimPlansGenerator:

    # Function: Constructor
    def __init__(self):

        # Build Halo spinner
        self.systemResponse = Halo(spinner='dots')

        # Build parser element
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", "-i", default="./resources/network.jpg", help="Input image network.")
        parser.add_argument("--database", "-d", default="./resources/database.csv",
                            help="Input database file.")

        # Parse arguments
        args = parser.parse_args()
        self.input = args.input
        self.database = args.database

    # Function: getSystemPlatform
    def getSystemPlatform(self):

        # Get system configuration
        print("\nDetecting system and release version ...\n")
        systemPlatform = platform.system()
        systemRelease = platform.release()

        print("**************************************************************************")
        print("Configuration detected:")
        print("**************************************************************************")
        print("\nPlatform:")
        print(systemPlatform)
        print("Release:")
        print(systemRelease)

        return systemPlatform, systemRelease

    # Function: getDatabase
    def getDatabase(self):

        # Read from file
        database = pd.read_csv(str(self.database), sep=";")

        print("Database:\n")
        print(database)

        return database

    # Function: getAdapterParams
    def getAdapterParams(self):

        # Get adapter params from input
        network = cv2.imread(str(self.input))
        height, width, channels = network.shape

        print("\nHeight: " + str(height) + ", Width: " + str(width))

        return height, width

    # Function: getDatabaseParams
    def getDatabaseParams(self, database):

        # Get max X and Y coordinate value
        max_X = 0
        max_Y = 0

        for coordinateX in database.X_INIT:
            if int(coordinateX) > max_X:
                max_X = int(coordinateX)

        for coordinateX in database.X_DEST:
            if int(coordinateX) > max_X:
                max_X = int(coordinateX)

        for coordinateY in database.Y_INIT:
            if int(coordinateY) > max_Y:
                max_Y = int(coordinateY)

        for coordinateY in database.Y_DEST:
            if int(coordinateY) > max_Y:
                max_Y = int(coordinateY)

        print("Max x: " + str(max_X) + ", Max Y: " + str(max_Y) + "\n")

        return max_X, max_Y

    # '" end_time="06:00" />\n'
    # '" dur="00:10" />\n'
    # Function: generatePlansFile
    def generatePlansFile(self, height, width, database, max_X, max_Y):

        try:
            path = "./plans.xml"
            file = open(str(path), 'w+')
            file.write('<?xml version="1.0" ?>\n')
            file.write('<!DOCTYPE plans SYSTEM "http://www.matsim.org/files/dtd/plans_v4.dtd">\n')
            file.write('<plans xml:lang="de-CH">\n')

            for (person, time_ends, duration) in zip(range(int(len(database.X_INIT))), database.TIME_DEST, database.DURATION):
                identifier = '<person id="' + str(int(person) + 1) + '">\n'
                file.write(str(identifier))
                file.write('<plan>\n')
                planner = '<act type="h" x="' + str(int(database.X_INIT[person])) + '" y="' + str(int(database.Y_INIT[person])) + '" end_time="' + str(database.TIME_DEST[person]) + '" />\n'
                file.write(str(planner))
                file.write('<leg mode="car">\n')
                file.write('</leg>\n')

                time_dur = int(database.DURATION[person])
                if time_dur >= 60:
                    time_dur = 59
                if time_dur < 10:
                    time_dur = 10

                planner = '<act type="w" x="' + str(int(database.X_DEST[person])) + '" y="' + str(
                    int(database.Y_DEST[person])) + '" dur="00:' + str(time_dur) + '" />\n'
                file.write(str(planner))
                file.write('<leg mode="car">\n')
                file.write('</leg>\n')

                planner = '<act type="w" x="' + str(int(database.X_DEST[person])) + '" y="' + str(
                    int(database.Y_DEST[person])) + '" dur="00:' + str(time_dur) + '" />\n'
                file.write(str(planner))
                file.write('<leg mode="car">\n')
                file.write('</leg>\n')

                planner = '<act type="h" x="' + str(int(database.X_INIT[person])) + '" y="' + str(int(database.Y_INIT[person])) + '" />\n'
                file.write(str(planner))

                file.write('</plan>\n')
                file.write('</person>\n')


            file.write('</plans>\n')
            file.close()

            systemResponseMessage = "\n[INFO] Plans file generated correctly.\n"
            self.systemResponse.text_color = "green"
            self.systemResponse.succeed(systemResponseMessage)

        except Exception as ex:
            systemResponseMessage = "\n[ERROR] Error, generating plans file.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)

    # Function: processRequests
    def processRequests(self, height, width, database, max_X, max_Y):

        print("\n**************************************************************************")
        print("Processing request:")
        print("**************************************************************************\n")

        try:
            # Get initial time
            initialTime = datetime.datetime.now()

            # Generate plans file
            self.generatePlansFile(height, width, database, max_X, max_Y)

            systemResponseMessage = "\n[INFO] Request done correctly.\n"
            self.systemResponse.text_color = "green"
            self.systemResponse.succeed(systemResponseMessage)

            # Get end time
            endTime = datetime.datetime.now()

            # Compute elapsed time
            elapsedTime = endTime - initialTime

            systemResponseMessage = "\n[INFO] Elapsed time: " + str(elapsedTime) + ".\n"
            self.systemResponse.text_color = "blue"
            self.systemResponse.info(systemResponseMessage)

        except:
            systemResponseMessage = "\n[ERROR] Error, processing request.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)


# Function: main
def main():

    print("**************************************************************************")
    print("**************************************************************************")
    print("                   Program: MATSim Plans Generator                        ")
    print("                     Author: David Velasco Garcia                         ")
    print("                             @davidvelascogarcia                          ")
    print("**************************************************************************")
    print("**************************************************************************")

    print("\nLoading MATSim Plans Generator engine ...\n")

    # Build matsimPlansGenerator object
    matsimPlansGenerator = MATSimPlansGenerator()

    # Get system platform
    systemPlatform, systemRelease = matsimPlansGenerator.getSystemPlatform()

    # Read database
    database = matsimPlansGenerator.getDatabase()

    # Get adapter params
    height, width = matsimPlansGenerator.getAdapterParams()

    # Get database params
    max_X, max_Y = matsimPlansGenerator.getDatabaseParams(database)

    # Process input requests
    matsimPlansGenerator.processRequests(height, width, database, max_X, max_Y)

    print("**************************************************************************")
    print("Program finished")
    print("**************************************************************************")
    print("\nmatsimPlansGenerator program finished correctly.\n")

    #userExit = input()


if __name__ == "__main__":

    # Call main function
    main()
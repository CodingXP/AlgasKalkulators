
# Paycheck Calculator

A calculator to which generates how much earnings will you get after tax by inputting the ammount you get on hand.

## Features

- Register and login functionality.
- Website to advertise.
- Fully working paycheck calculator.
- Exporting calculated paycheck to .pdf on your computer.


## Run Locally

1. Clone the project

```bash
  git clone https://github.com/CodingXP/AlgasKalkulators.git
```

2. Open command prompt in the project location

```bash
  cd project-download-location
```

3. Install dependencies

```bash
  py -m pip install mysql-connector-python
  py -m pip install pyqt6
  py -m pip install reportlab
```

4. Start the Webserver and local database


5. Create the database

```bash
CREATE DATABASE paycheck;
USE paycheck;

CREATE TABLE userdata(
	name char(20),
    surname char(20),
    email char(30),
    password char(20),
    primary key (email)
)
```

6. Run the program

```bash
  py pcalc.py
```

# Made by DP3-2 (Gustavs Vistins, Nikita Palcevskis, Eduards Novasads)

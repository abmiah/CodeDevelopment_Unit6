### GitHub Repository
`https://github.com/abmiah/CodeDevelopment_Unit6.git`

### Video demonstration
`https://youtu.be/Av_VLlPn6bo`

## 1.	Introduction 

This README documentation presents a comprehensive examination of the evolution of initial collaborative efforts that 
culminated in the development of the Attack-Defence Tree (AD) within the context of a System of Systems (SoS) framework. 
The analysis is informed by a case study conducted by Kodali et al. (2016), which identifies various vulnerabilities associated 
with the IoT, employing the AD tool to uncover potential weaknesses. This inquiry is particularly pertinent to the domain of IoT, 
with a specific focus on a smart home security system that utilises Wi-Fi technology to notify users of unauthorised access attempts. 
This IoT device functions as an integrated network of multiple SoS, encompassing an array of interconnected sensors and cameras
managed through a centralised hub.

Given the vulnerabilities revealed in the AD analysis, one must develop a hypothesis grounded in one of the ABCDE 
methodologies: autonomy, belonging, connectivity, diversity, and emergence (Boardman & Sauser, 2006). This document will 
analyse a specific methodology and its relation to the hypothesis with a code output and provide an overview of the code 
and its documents. 

The hypothesis will be predicated on the default password used within the central hub, as found in the AD analysis. 
The code is implemented in Python, using object-oriented programming (OOP) principles. This methodology will rigorously 
evaluate the proposition by conducting a series of tests to verify the integrity of the password as a viable mitigation 
strategy.

## 2.	Default Password

Manufacturers developing Internet of Things (IoT) devices frequently establish default passwords, known as universal default 
passwords (UDPs). The rationale behind manufacturers' implementation of UDPs is multifaceted. According to Cybertechaccord (2024), 
one primary objective for instituting UDPs is facilitating device accessibility when users inadvertently become locked out. 
Furthermore, UDPs enable engineers to conduct updates and perform diagnostic testing on devices effectively.  However, UDP 
settings have several vulnerabilities that open them to attacks.  According to Borgeaud (2023), one of the most common IoT 
default passwords is “`admin`”. 

From 2022 to 2024, the UK enacted new legislation under the Conservative government to enhance cybersecurity protocols. 
This legislative framework prohibits manufacturers from establishing weak, easily predictable passwords while permitting 
users to modify the default password allocated during the initial configuration (GOV.UK, 2024).

## 3.	Methodology 

Boardman and Sauser (2006) state the intricacies associated with system design, particularly in the context of SoS. 
They highlight the critical significance of managing the connectivity between various systems and subsystems. 
A fundamental principle for engineers is the continual reduction of interfaces among subsystems; however, this principle 
encounters substantial challenges in SoS environments, especially when integrating legacy systems with contemporary and 
developing systems. Ensuring interoperability may necessitate the revelation of certain internal connections, which are 
conventionally obscured at the system's boundaries. Additionally, it is significant that legacy systems frequently employ 
default passwords, a factor that presents considerable security risks, particularly when IoT devices are integrated into 
the network.

## 4.	Code output 

This project constitutes a comprehensive password assessment tool designed to evaluate the strength and security of 
administrative passwords. It systematically compares the provided password against a database of commonly compromised 
passwords derived from the NCSC (2012). The assessment encompasses an analysis of the password's length and character 
diversity. If the password is weak, the program generates an alternative password. Furthermore, the project incorporates 
an authentication server dedicated to verifying password attempts.

The primary objective of the script is to guarantee the security of the initial administrator password designated for 
the IoT Hub. It conducts a series of evaluations to assess the robustness of the password and implements strategies to 
address vulnerabilities associated with weak passwords by generating new, more robust alternatives.

## 4.1.	Key characteristics of the script.

- **Comparing the password against NCSC pwned passwords:** This function evaluates the presence of the specified password within the NCSC `PwnedPasswordsTop100k.txt` database file. 
- **Encrypting password:** SHA-256 encryption from the `hashlib` library is used to hash the password.
- **Length of the password and character types used:** Ensure the password meets the requisite length and complexity requirements criteria. 
- **Password mitigation is found to be weak:** Generates a novel, randomly generated password upon the replacement of the current one weak. Authentication server: Establishes a fundamental authentication server designed to assess and verify password submission attempts.

## 4.2.	System Requirements. 

- Python 3.11.3 (The code has been developed using the latest version of Python; therefore, older versions may not be capable of executing the script effectively)
- `Requests` library: this library retrieves the NSCS (2012) `PwnedPasswordsTop100k.txt` file using the requests library to fetch data.- `pip install requests`
- `Colorama` library is primarily aimed at enhancing visual presentation during console output, thereby facilitating improved readability. - `pip install colorama` 

## 4.3.	Clone repository.

You can clone the initial code from the GitHub repository using the following link: `https://github.com/abmiah/CodeDevelopment_Unit6.git`.

## 4.4.	Running the script

1)	Run the main script `mainScript_CheckPassword.py`: 
2)	Follow the prompts to set an admin password, and enter a common password such as `password123`, `qwert`, or `admin`.
3)	The script will start an authentication server and perform various checks on the password.

## 4.5.	Script Descriptions

- `adminPassword.py`: Manages the configuration of the admin password and initiates the authentication server.
- `pwnedPasswordCheck.py`: Verifies whether the password appears in the NCSC `PwnedPasswordsTop100k.txt` file.
- `hashPassword.py`: Hashes the password using SHA-256 and checks if the password is valid hashed.
- `passwordCount.py`: Assesses the password's length and character types to determine its strength.
- `newPassword.py`: Creates a new random password in case the existing one is weak.
- `mainScript_CheckPassword.py`: This is the primary script responsible for managing password verification process.

## 4.6.	Classes and Methods Overview 

### adminPassword.py.

-	`AdminPassword`: Admin password and authentication management class server.
-	`load_weak_passwords()`: Retrieves a collection of insecure passwords from a URL.
-	`is_weak_password(password)`: Verifies the validity of a password weak.
-	`start_auth_server()`: Initiates the authentication process server.
-	`stop_auth_server()`: Halts the authentication process server.

### pwnedPasswordCheck.py.

-	`PwnedURL`: Class for verifying if a password appears in `PwnedPasswordsTop100k.txt` file.
-	`get_password_list()`: Obtains the list of compromised accounts passwords.

### hashPassword.py.

-	`PasswordHash`: A class for hashing and verification of passwords.
-	`hash_password(password)`: Applies hashing to a password using SHA-256.
-	`is_password_hashed(password)`: Verifies if a password is hashed.
-	`print_hashed_password()`: Outputs the hashed information password.

### passwordCount.py.

-	`PasswordCount`: Evaluate the length and types of characters within a string password.
-	`count_password_length(password)`: Counts the length of a string password.
-	`print_password_length()`: Prints the length of a password.
-	`check_character_types(password)`: Checks the character types of a password.
-	`print_character_types()`: Displays the types of characters in a password.
-	`evaluate_password_strength()`: Evaluate the potency of a password.
-	`print_password_strength()`: Outputs the strength of a password.
-	`is_password_weak()`: Verifies the validity of a password weak.

### newPassword.py.

-	`NewPassword`: Class for creating a new random password.
-	`random_password(length)`: Creates a random password that is 25 characters in length characters.
-	`print_password()`: Outputs the new random password.

### mainScript_CheckPassword.py.

The main program executes the script within the console environment. It systematically invokes all the ancillary files 
essential for the program's operational functionality. It also employs `threading` to initiate the authentication server 
in an isolated thread. 

-	`PasswordChecker`: Examines the different aspects of the admin password.
-	`check_password_from_pwned()`: Verifies if the password appears in the `PwnedPasswordsTop100k.txt`.
-	`check_password_hashed()`: Verifies whether the password is hashed.
-	`check_password_length()`: Evaluate the password's length and character types.
-	`new_password()`: Creates and prints a new random password when the existing password is weak.

## 5.	Reference:

Boardman, J. and Sauser, B. (2006). System of Systems - the meaning of of. 2006 *IEEE/SMC International Conference on 
System of Systems Engineering*. [online] doi:https://doi.org/10.1109/sysose.2006.1652284 [Accessed 24 Nov. 2024].

Borgeaud, A. (2023). *Frequently seen passwords in IoT devices 2021*. [online] Statista. 
Available at: https://www.statista.com/statistics/1298495/frequently-seen-passwords-in-iot-devices/ [Accessed 25 Nov. 2024].

Cybertechaccord (2024). *No Universal Default Passwords*. [online] Cybertechaccord.org. 
Available at: https://cybertechaccord.org/no-universal-default-passwords/ [Accessed 25 Nov. 2024].

GOV.UK (2024). *New laws to protect consumers from cyber criminals come into force in the UK*. [online] GOV.UK. 
Available at: https://www.gov.uk/government/news/new-laws-to-protect-consumers-from-cyber-criminals-come-into-force-in-the-uk [Accessed 25 Nov. 2024].

Hartley, J. (2022). *colorama: Cross-platform Colored Terminal text*. [online] PyPI. Available at: https://pypi.org/project/colorama/ [Accessed 18 Nov. 2024].

Jain, Y. (2023). *How to Print Colored Text in Python - Studytonight*. [online] www.studytonight.com. 
Available at: https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python [Accessed 18 Nov. 2024].

Miessler, D. (2022). *10-million-password-list-top-10000.txt*. [online] GitHub. 
Available at: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt [Accessed 17 Nov. 2024].

NCSC (2012). *PwnedPasswordsTop100k.txt*. [online] Ncsc.gov.uk. 
Available at: https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt [Accessed 16 Nov. 2024].

Python (2020a). *socket — Low-level networking interface — Python 3.8.1 documentation*. [online] Python.org. 
Available at: https://docs.python.org/3/library/socket.html [Accessed 20 Nov. 2024].

Python (2020b). *threading — Thread-based parallelism — Python 3.9.0 documentation*. [online] docs.python.org. 
Available at: https://docs.python.org/3/library/threading.html [Accessed 20 Nov. 2024].

Python (2024). *hashlib — Secure hashes and message digests — Python 3.8.4rc1 documentation*. [online] docs.python.org. 
Available at: https://docs.python.org/3/library/hashlib.html [Accessed 17 Nov. 2024].

python.org (2024). *string — Common string operations — Python 3.9.1 documentation*. [online] docs.python.org. 
Available at: https://docs.python.org/3/library/string.html [Accessed 18 Nov. 2024].

Reitz, K. (2023). *requests: Python HTTP for Humans*. [online] PyPI. Available at: https://pypi.org/project/requests/ [Accessed 16 Nov. 2024].
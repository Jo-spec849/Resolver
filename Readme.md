![Banner Shodan](https://raw.githubusercontent.com/Jo-spec849/Resolver/main/Prints/shodan.png)
Fast Enumeration Tool using Shodan
=================================================

This is a Python script developed to assist in the reconnaissance process during a penetration test. During collaboration with the PROOF team, I identified the need for a tool that would perform a quick initial enumeration while other tools, such as nmap, were running. Based on this need, I created this script that utilizes the data available in Shodan to perform a rapid enumeration, leveraging the information already collected by the platform.

Shodan and its use
----------------

Shodan is a search engine that allows you to find devices connected to the internet, including servers, IP cameras, routers, and more. Unlike traditional search engines, Shodan focuses on finding specific devices rather than web pages. It indexes information about the services running on the devices, such as open ports, banners, and other detailed information. This can be extremely useful for security professionals as it allows for identifying potential targets and assessing the exposure of internet-connected devices.

History
--------

During a penetration test collaboration with the PROOF team, I encountered the need for a tool that would provide a quick initial enumeration while other tools were running. This initial enumeration could provide valuable information that could be used to target efforts during the test.

That's when I decided to create this Python script that utilizes the data available in Shodan to perform a quick initial enumeration. It leverages the information already collected by the Shodan platform, such as open ports and details of the device's owning organization. This information is crucial to finding other hosts belonging to the same organization and exposed on the internet. Additionally, the script performs active host checking to provide a more up-to-date overview.

The script stores all the collected information in an organized spreadsheet, allowing for easy analysis and understanding of the results. It will also include the functionality to capture screenshots of the homepages of the identified sites, facilitating their visualization and subsequent analysis.

Current and future features
--------------------------------

The main current features of the script include:

* Rapid enumeration of hosts using Shodan.
* Gathering of open ports and details of the owning organization.
* Active host checking.
* List of vulnerabilities present in the services that are known to Shodan.
* Storage of information in a spreadsheet.
* Storage of the JSON data of the performed queries.
* Choice of output format: CSV or XLSX.

Planned features for future versions of the script include:

* Implementation of a function to access the hosts and capture screenshots of the homepages of the identified sites.
* Inclusion of the protocol used for each identified port.
* Inclusion of the banners of the found services.
* Gathering of known links from The Wayback Machine for all provided targets.

These improvements aim to provide a more comprehensive view and facilitate the reconnaissance process during a penetration test.

Using the script
--------------------

1. Make sure you have Python installed on your system.
2. Download the script's source code from the following repository: \[REPOSITORY URL\].
3. Open the terminal or command prompt and navigate to the directory where the script is saved.
4. Run the script using the following command:
    
      
    ```bash
    python3 resolver-banners.py  -h
    ```

Here are some screenshots demonstrating the use of the script:

1. Running the script with the `-h` option to display the command's help:
    
    ![Script execution](https://raw.githubusercontent.com/Jo-spec849/Resolver/main/Prints/help.png)
    
2. Running the script with the input file and API key arguments:
    
    ![Running with input file and API key](https://raw.githubusercontent.com/Jo-spec849/Resolver/main/Prints/run.png)
    
3. Results saved in a spreadsheet (XLSX or CSV format):
    
    ![Results spreadsheet](https://raw.githubusercontent.com/Jo-spec849/Resolver/main/Prints/output.png)
    

The reconnaissance process is an essential step in a penetration test. It allows for collecting valuable information about the targets, identifying potential vulnerabilities, and devising appropriate strategies for the remainder of the test. The developed tool aims to automate part of this process by providing a quick and organized enumeration of hosts, facilitating further analysis.

Please note that this is an initial version of the tool, and new features and enhancements are planned for future versions.

Acknowledgements
--------------------

I would like to thank my colleague Gabriel Comonian for his collaboration in the initial testing of the script, and the GPT chat for their assistance in the development.

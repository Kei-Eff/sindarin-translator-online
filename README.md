CCC-2022 T4A2 - Full Stack Application - Karl Alberto

---

___N.B. Edited/updated from original prject and documentation [here](https://github.com/Kei-Eff/T4A2_Final) due to shift in tech stack.___

# Sindarin Translator Online

![Sindarin Translator Online title](./docs/img/sto_title.png)

## Description

_Sindarin Translator Online_ aims to provide a web interface for the terminal application I created in Term 2 (2021) for the CCC course (T2A3). You can find more details about that project [here](https://github.com/Kei-Eff/sindarin-translator).

Documentation and Development updates are available via Trello [here](https://trello.com/b/5FlPl44f/t4a2-sindarin-translator-online), along with screenshots below.

Website will be hosted on `Amazon EC2`; built with `Python` using `Flask` web framework. Frontend is `HTML5` with `Pico.css` framework. `Amazon DynamoDB` will be used as a cache for translations, with a 24-hour _Time-To-Live (TTL)_ setting. `AWS IAM` and `AWS Parameter Store` are used for account management and secret key storage, respectively. Version control is handled by `Github`.

<br>


## Main Functionality/Features

* English-to-Sindarin (Tolkien _Elvish_) translations
* Easy to use, responsive website
* Minimal design: text in, text out
* Cache for recently requested translations (to limit API calls)

## Future Improvements/Additional Features

* More Middle Earth language options:
    * English-to-_Quenya_
    * English-to-_Orcish_
* Output text in _Tengwar_ (Elvish) script

<br>


## Target Audience

* Fans of J.R.R. Tolkien's written works, and the 'Middle Earth'/'Lord of the Rings' universe.
* Fans of the 'Lord of the Rings' and 'The Hobbit' movie franchises.
* Fans who are interested in the upcoming 'Rings of Power' _Amazon Prime Video_ series.
* Fans of _Conlangs_ (Constructed Languages) who want a phonetic representation of the _Elvish Sindarin_ language.
* Linguists and linguistics students who want to study how Tolkien created his own languages.
* Fans of video games set in Middle Earth.

<br>


## Tech Stack

* HTML5
* CSS ([Pico.css](https://picocss.com/))
* Python 3
* Flask
* Github
* AWS Identity and Access Manager
* AWS EC2
* Amazon DynamoDB
* AWS Parameter Store

<br>


## Dataflow Diagram

Dataflow Diagram still reflects current dataflow, per Part A of assignment:

![STO Dataflow Diagram](./docs/img/sto_dataflow_diagram_v2.png)

PDF version available [here](https://drive.google.com/file/d/12M_AjIVeAlF6yyiZiKg_ZUP8SYS7ouDh/view?usp=sharing).

<br>


## Application Architecture Diagram

Updated Application Architecture Diagram to reflect changes to tech stack and deployment method:

![STO Application Architecture Diagram; current as at 11.03.2022](./docs/img/sto_app_architecture_v2.png)

PDF version available [here](https://drive.google.com/file/d/1odDpjlFZMSXDsTBObDBD38MtVnnjkr5f/view?usp=sharing)

<br>


## Progress Updates: Trello

_N.B. Updates from February 2022 can now be found [here](./docs/trello_updates_feb_2022.md)._

Priority labels as follow:

    * Low Priority
    * Priority (default)
    * High Priority
    * Urgent
    * Ongoing
    * Nice to Have
    * CRITICAL
    * Postponed


### 1 March 2022

Tackling page layout:

![Trello Board at 1 March 2022 - Coding start](./docs/img/trello/mar_2022/Trello_01.03.2022a.png)

___Trello highlights between 1-6 March can be found in the original [project repo](https://github.com/Kei-Eff/T4A2_Final).___


### 7 March 2022

Updated tech stack and app direction; Trello tasks updated with dates, new list and labels (for "Postponed" tasks). No longer serverless due to time constraints. Moving back to `Flask` on _EC2_ deployment:

![Trello Board at 7 March 2022 - Task updates](./docs/img/trello/mar_2022/Trello_07.03.2022a.png)


### 8 March 2022

Readme updates; created `Table` in _Amazon DynamoDB_:
![Trello Board at 8 March 2022 - Task updates](./docs/img/trello/mar_2022/Trello_08.03.2022a.png)


### 9 March 2022

Flask app running on _EC2_:

![Trello Board at 9 March 2022 - Task updates](./docs/img/trello/mar_2022/Trello_09.03.2022a.png)


### 10 March 2022

Set up DynamoDB connection + caching:

![Trello Board at 10 March 2022 - Task updates](./docs/img/trello/mar_2022/Trello_10.03.2022a.png)


### 11 March 2022

AWS Parameter Store work + Python `unittest`:

![Trello Board at 11 March 2022 - Task updates](./docs/img/trello/mar_2022/Trello_11.03.2022a.png)

Adding final touches, deploying to EC2:

![Trello Board at 11 March 2022 - Task updates](./docs/img/trello/mar_2022/Trello_11.03.2022b.png)


---


## Milestones and Testing

### 4 March 2022

API Gateway; and Lambda API endpoint testing:

![Testing API Gateway - 4 March 2022](./docs/img/milestones/API_Gateway_Testing_04.03.2022a.png)

![Testing API Gateway - 4 March 2022](./docs/img/milestones/API_Gateway_Testing_04.03.2022b.png)

![Testing API Gateway - 4 March 2022](./docs/img/milestones/Lambda_Testing_04.03.2022a.png)


### 8 March 2022

Testing API Error Message on page:

![Testing API error messages - 8 March 2022](./docs/img/milestones/ErrorTesting_SindarinAPI_08.03.2022a.png)


### 9 March 2022

Working _"Tengwar"_ message output. Added 'About' page, with site credits:

![Tengwar Output and About Page - 9 March 2022](./docs/img/milestones/Added_About_Page_09.03.2022.png)

![Tengwar Output - 9 March 2022](./docs/img/milestones/TengwarFont_Working_09.03.2022.png)

Live Site Tests:

Chrome

![Live on Chrome Browser - 9 March 2022](./docs/img/milestones/LiveSiteTest_Chrome_09.03.2022a.png)

![Live on Chrome Browser - 9 March 2022](./docs/img/milestones/LiveSiteTest_Chrome_09.03.2022b.png)

![Live About Page on Chrome Browser - 9 March 2022](./docs/img/milestones/LiveSiteTest_AboutPage_09.03.2022a.png)

Firefox

![Live on Firefox Browser - 9 March 2022](./docs/img/milestones/LiveSiteTest_Firefox_09.03.2022a.png)

![Live on Firefox Browser - 9 March 2022](./docs/img/milestones/LiveSiteTest_Firefox_09.03.2022b.png)

Tablet (iPad Air)

![iPad screen size - 9 March 2022](./docs/img/milestones/LiveSiteTest_Tablet_09.03.2022a.png)

iPhone (12 Pro)

![iPhone screen size - 9 March 2022](./docs/img/milestones/LiveSiteTest_iPhone_09.03.2022a.png)

Android (Samsung Galaxy S20 Ultra)

![Android screen size - 9 March 2022](./docs/img/milestones/LiveSiteTest_Android_09.03.2022a.png)


### 10 March 2022

Added error handling for empty strings (to prevent API calls):

![Empty message error handling - 10 March 2022](./docs/img/milestones/EmptyMessageError_10.03.2022a.png)

Testing DynamoDB connection:

![DynamoDB connection test](./docs/img/milestones/DynamoDB_Test_Connection_10.03.2022a.png)

![DynamoDB connection test](./docs/img/milestones/DynamoDB_Test_Connection_10.03.2022b.png)

Using `Flask` `app.logger` to check connections via terminal:

![Flask app logger](./docs/img/milestones/DynamoDB_Test_FlaskAppLogger_10.03.2022a.png)

Successful DynamoDB tests:

![DynamoDB test](./docs/img/milestones/DynamoDB_Test_Success_10.03.2022a.png)

![DynamoDB test](./docs/img/milestones/DynamoDB_Test_Success_10.03.2022c.png)

![DynamoDB test](./docs/img/milestones/DynamoDB_Test_Success_10.03.2022c.png)


### 11 March 2022

Unittest using `boto3` + `moto` ([moto repo](https://github.com/spulec/moto)) package to mock DynamoDB connection:

![Testing cache connection](./docs/img/milestones/Cache_Unittest_11.03.2022a.png)

Manual testing new messages + `app.logger` for triggering API calls, then cache results:

![Testing API and cache calls](./docs/img/milestones/Testing_API_Call_Caching_11.03.2022a.png)


---

Karl Alberto | 2022
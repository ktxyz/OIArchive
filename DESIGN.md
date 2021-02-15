# OIArchive - Design Document

## Philosophy and objectives of this project

OIArchive is in its simplest form a searchable list of competetive programming problems and tasks. Our objective is to empower teachers, students and contests creators with tools that allow them to easily find probles to either teach, learn or get inspired by. Every problem should be explained IN-DEPTH. With many hardness scales presented, summary of story and technical problem and different solutions every problem can be quickly understood in its basic core which from our experience is very important both for teachers searching for problems for their students, as well as students looking to train their skills. We are striving to be a truly useful tool, thats why we believe that everything should be publicly available to everyone, the ranking if it exists is not to compare yourself to others but to track your progress. We believe in honesty of our users since it's in their greatest interest to actually learn those problems - they wont get anything from us either way so they can only hope to succeed in some contest. Everything of importance HAS to be plaintext for ease of later searching for it.

## Design descriptions

### Problems [MVP]

#### Problem rules
* Every problem has some judge system where people can freely test their solutions (if the judge becomes inactive, the problem shall be archived until a new one becomes available)

#### Problem structure
Every problem requires following elements:

* Title
* unique ID
* Link to publicly available judge system
* Short story summary
* Short technical problem summary (what has to be done explained in more strict language)
* 2 hardness ratings (difficulty to come up with solution, difficulty to implement the solution)
* User who originally submitted this problem
* Moderator who published this problem

Every problem can contain following elements:

* Comments of users about this task
* Tags based on techniques and difficulty
* Solutions based on different ideas(they require big changes, otherwise should be submitted as notes to original solution) explained in-depth either with source code provided or not.

### Lists [MVP]

Lists should be treading in OIArchive system as sort of a playlist or rather a semi-fledged forum. It's main goal is to provided teachers with centralized place to share tasks with their students. A list can have seperate sections (i.e topics or different lessons) all modifiable by the user. All lists are public but they can be changed only by the creator.

#### Lists structures

Every list requires following elements:

* Title
* unique ID
* List owner

Every list can contian following elements:

* Special sections grouping
* assigned forum
* Assigned problems (if some problems don't have section assigned to them and some section exists, they should be classified as Unassigned)


#### List sections structures
Every list section requires following elements:

* Title

Every list can contain following elements:

* Assigned forum
* Assigned problems


### Forums [MVP]

Forums are supposed to be mostly assigned, there will be also a single big forum. Forums can be added to lists and can be set as to a private mode where owner of the list can whitelist / blacklist certain users from commenting. Forum usage requires an account.

#### Threads

Each forum can have threads created in different modes (auto / moderated). Each thread can be archived, but can't be deleted.

#### Comments

Each thread contains comments that can be added in different modes (auto / moderated). Each comment can be removed by forum owner or administrator.

When you comment in a thread you automatically (based on preferences) subscribe to news feed about the discussion. You can always mute a thread.

### Solutions [MVP]

A solution should be an in-depth explanation of solving process for a problem. It should contain steps and clues about coming to a solution by yourself. It should not contain proofs for well known algorithms (it should link to outside sources instead).


#### Solution structure
Each solution has to contain:

* Author
* Body written in markdown
* Source code implementing the solution
* Rating of hardness to implement / understand

Each solution can contain

* Tags for ease of searching the database

### Submition

Each user can submit any solved problem and get it acclaimed by moderation.

#### Manual submition [MVP]

##### Manual submition structure

Every manual submition should contain:

* Source code
* Screenshot of received points by a judge system

##### Submission result

Each submission is either accepted (after being checked by moderator) or discarded with comment about the decision.

#### Automatic submition

TODO

### Users [MVP]

Every user should have own profile with username, his a age (can be unspecified) and his country (can be unspecified).
On user's profile page all accepted submission will be shown as well as some simple statistics.

#### Statistic:

* Language usage
* Avg. code length
* Avg. score per task
* Number of tasks
* Avg task difficulty
* Number of comments and number of threads
* Public lists

### User submited content
#### Manualy submitted content [MVP]

Users can manually submit content.

### Changes history, reverting and moderating [MVP]



### Various assumptions [MVP]

* Site is bilingual [ENG, POL]
* Site is protected from spam by home-made captcha like system
* Site doesn't track its users, all analitycs should be home-made
* Site is and will be free to use
* Main goal for me to sustain the website would be through donations
* No advertisments
* Content provided to the site (original) is licensed by GPL and belongs to the author but he can't remove it.

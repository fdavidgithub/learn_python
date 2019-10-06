# Create output as a OUTER JOIN (SQL) using csv file
If verb on Past participle is equal to simple past, do not save in output file

* simple_past.csv: list of irregular verbs the [simple past](https://en.wiktionary.org/wiki/simple_past)
* past_participle.csv: list of irregular verbs the [past participle](https://en.wiktionary.org/wiki/past_participle)

# File structure
* simple_past.csv\
    [verb present/future];[verb simple past]
* past_participle.csv\
    [verb present/future];[verb past participle]

# Examples
| Verb  | Simples past | Past participle |
|-------|--------------|-----------------|
| drink | drank        | drunk           |
| buy   | bought       | bought          |
| put   | put          | put             |

**Verbs that do not change (e.g put) are not present in the files**

![Common verbs](sets.png "Groupss")

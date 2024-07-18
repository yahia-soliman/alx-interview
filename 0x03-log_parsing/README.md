# Log Parsing

the format of a log entry:
```sh
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

we need to extract some data from this line:

- status code
- file size

having this data about each log record print a statistics of all the logs you read after every 10 requests.

the stats is:
total <file size>
for each status code, how many time a status code is called, sorted descending?

# regular expression matching
We need to parse the needed data from the log record
```regex
^
((1?\d?\d|2[0-4]\d|25[0-5])(\.| - )){4}     #<IPv4>
\[\d.+\d\]                                  #<date>
 "GET /projects/260 HTTP/1.1"               #exact
 ([2-5]0[0-5])                              #status code
(\d+)                                       #file size
$
```

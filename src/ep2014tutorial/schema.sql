create table tweets (
 id string primary key,
 created_at timestamp,
 text string INDEX using fulltext,
 source string INDEX using fulltext,
 retweeted boolean,
 "user" object(strict) as (
        created_at timestamp,
        verified boolean,
        followers_count integer,
        id string,
        statuses_count integer, \
        description string INDEX using fulltext, \
        friends_count integer, \
        location string INDEX using fulltext \
        )
) with (number_of_replicas = '0-5');

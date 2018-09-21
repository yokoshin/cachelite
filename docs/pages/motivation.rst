
Motivation
----------
This library is a sub-product of my "WEB-CRAWLING" job.
There are many cache libraries, but most of them are memory-based. I like to use file-based one.
Also many cache libraries are thread-safe not multi-process-safe. I like to use multi-process-safe one.

Idea
----
This implementation is inspired by Cache_Lite(https://pear.php.net/package/Cache_Lite/)
Each key-value pair is stored in the "md5(key).pkl" in your cache dir.
To make strictly process-safe, and thread-safe is difficult, but "almost" is easy.
The design of the number of parallelization is at most 10.



---
layout: post
title: Java Puzzle #3: Rounding
author: Martin Thoma
date: 2012-07-17 17:00:53.000000000 +02:00
category: Code
tags: Programming, Java, puzzle
featured_image: 2012/07/java-thumb.png
---
<h2>The puzzle</h2>
What is the output of the following script:
```java
public class test {
    public static void main(String[] args) {
        double x = 0.4999999999999999;
        double y = 0.49999999999999992;
        double z = 0.49999999999999994;
        System.out.println(x + " rounded is " + Math.round(x));
        System.out.println(y + " rounded is " + Math.round(y));
        System.out.println(z + " rounded is " + Math.round(z));
    }
}
```


.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

<h2>Answer</h2>
```bash
0.4999999999999999 rounded is 0
0.49999999999999994 rounded is 1
0.49999999999999994 rounded is 1
```

<h2>Explanation</h2>
It's a <a href="http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6430675">bug</a>. 

See also: <a href="http://stackoverflow.com/q/9902968/562769">Why does Math.round(0.49999999999999994) return 1</a>

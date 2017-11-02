<!DOCTYPE html>
<div>
  <h2>Intro to Hadoop and MapReduce - Udacity</h2>
  <p>Link to the course-- </p><p><a href="https://classroom.udacity.com/courses/ud617">https://classroom.udacity.com/courses/ud617</a></p>
  <p>The codes in this repo are only related to the project section in the course of the udacity and are meant to help people who are not able to solve the problems.</p>
  <h3>Question I</h1>
  <hr>
  <p>The three questions about this data set are:</p>
  <ul>
    <li>Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.</li>
    <li>Find the monetary value for the highest individual sale for each separate store.</li>
    <li>Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.</li>
  </ul>
</div>
<div>
  <div>
    <div>
      <h3>Question II</h1>
      <hr>
      <p>The data set we're using is an anonymized Web server log file from a public relations company whose clients were DVD distributors. The log file is in the udacity_training/data directory, and it's currently compressed using GnuZip. So you'll need to decompress it and then put it in HDFS. If you take a look at the file, you'll see that each line represents a hit to the Web server. It includes the IP address which accessed the site, the date and time of the access, and the name of the page which was visited.</p>
      <p>The logfile is in <a target="_blank" href="http://en.wikipedia.org/wiki/Common_Log_Format">Common Log Format</a>:</p>
      <pre><code><span class="hljs-number">10.223</span><span class="hljs-number">.157</span><span class="hljs-number">.186</span> - - [<span class="hljs-number">15</span>/Jul/<span class="hljs-number">2009</span>:<span class="hljs-number">15</span>:<span class="hljs-number">50</span>:<span class="hljs-number">35</span> -<span class="hljs-number">0700</span>] <span class="hljs-string">"GET /assets/js/lowpro.js HTTP/1.1"</span> <span class="hljs-number">200</span> <span class="hljs-number">10469</span>%h %l %u %t \<span class="hljs-string">"%r\" %&gt;s %b</span>
      </code></pre><p>Where:</p>
      <ul>
        <li>%h is the IP address of the client</li>
        <li>%l is identity of the client, or "-" if it's unavailable</li>
        <li>%u is username of the client, or "-" if it's unavailable</li>
        <li>%t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]</li>
        <li>%r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.</li>
        <li>%&gt;s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes <a target="_blank" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html">in W3C.org</a></li>
        <li>%b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.</li>
      </ul>
      </div>
    </div>
  </div>
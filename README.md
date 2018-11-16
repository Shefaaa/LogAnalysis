
# Logs Analysis Project
create a reporting tool that prints out reports based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database

<h3>Technologies Used</h3>
<ul>
  <li><a href="https://www.python.org/" target="_blank">Python 3 </a>- Language the project is coded in</li>
  <li><a href="https://www.vagrantup.com/" target="_blank">Vagrant </a>- For a dev VM</li>
  <li><a href="https://www.virtualbox.org/" target="_blank">VirtualBox </a>- Required for Vagrant</li>
  <li><a href="https://git-scm.com/" target="_blank">Git </a>- Source code management</li>
</ul>


<h3>System setup and how to view this project</h3>
<ul>
  <li>Download and install Vagrant</li>
  <li>Download and install Virtual Box</li>
  <li>Clone this repository</li>
  <li>Download the newsdata.sql from <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip" target="_blank">here</a></li>
  <li>Run <code>vagrant up</code> command to start up the VM</li>
  <li>Run <code>vagrant ssh</code> command to log into the VM.</li>
  <li><code>cd /vagrant </code>to change to your vagrant directory</li>
  <li><code>psql -d news -f newsdata.sql </code>to load the data</li>
  <li>Run <code>python logAnalysis.py</code></li>
</ul>

<strong>The Data Base Include Three tables:</strong>
<ul>
<li>articles (author, title, slug, lead, body, time, id)</li>
<li>authors (name, bio, id)</li>
<li>log (path, ip, method, status, time, ip)</li>
</ul>

<h3>Helpful Resources</h3>
<ul>
  <li><a href="https://www.python.org/dev/peps/pep-0008/">PEP8 style guide</a></li>
  <li><a href="https://github.com/otsop110/logs-analysis-project">logs-analysis-project</a></li>
  <li><a href="https://github.com/aviaryan/ud-logs-analysis">ud-logs-analysis</a></li>
</ul>  

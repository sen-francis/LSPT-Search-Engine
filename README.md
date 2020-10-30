# LSPT-Text-Transformation

**Text Transformation** is part of a search engine being designed as part of the LSPT course during Fall 2020. The component will take HTML documents and perform text-transformation on it essential for the search engine to work effectively. The component acts as a service that does not need to build any APIs of its own but plays an important role for other services to function properly. The transformation generated will form the basis of searching, querying, indexing, ranking and more.

## Data Flow

The flow of data across various teams concerned with the **Text Transformation** component are described below:
1. The Crawling team crawl HTML documents from the web and store all the documents in the **Document Data Source** database.
2. The **Text Transformation** component sends a request (at a regular interval, say, once every day) to the **Document Data Store** team's API to pull all recently crawled/updated HTML documents.
3. The HTML pages are received by the **Text Transformation** component. Text transformation is performed on each page such as HTML tag identification, lemmatization, n-gram identification etc.
4. The results are then sent to the database at the **Document Data Source** where all the text transformation is stored along with the webpage information.
5. The indexing team independently calls the **Document Data Storage** as and when they need to do indexing.

## Team Members

#### Team P
<ul>
	<li>Karan Bhanot (bhanok) - Team Leader</li> 
	<li>Tim Budding (buddit)</li>
	<li>Sen Francis (francs2)</li>
	<li>Zachary Koo (kooz2)</li>
</ul>

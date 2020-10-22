# LSPT-Text-Transformation

**Text Transformation** is part of a search engine being designed as part of the LSPT course during Fall 2020. The component will take HTML documents and perform text-transformation on it essential for the search engine to work effectively. The component acts as a service that does not need to build any APIs of its own but plays an important role for other services to function properly. The transformation generated will form the basis of searching, querying, indexing, ranking and more.

## Data Flow

The flow of data across various teams concerned with the **Text Transformation** component are described below:
1. The **Crawling** teams crawl HTML documents from the web and store all the documents in the **Document Data Source** database. They maintain a list of recently crawled webpages.
2. The **Text Transformation** component sends a request (at a regular interval, say, every 2 hours) to the **Crawling** team's API and returns a list of *pageIDs* of the recently crawled webpages.
3. The **Text Transformation** component sends a request to the **Document Data Source** to send all HTML documents corresponding to the list of *pageIDs*.
4. The HTML pages are received by the **Text Transformation** component. Text transformation is performed on each page such as HTML tag identification, lemmatization, n-gram identification etc.
5. The results are then sent to the database at the **Document Data Source** where all the text transformation is stored along with the webpage information.
6. The indexing team independently calls the **Document Data Storage** as and when they need to do indexing.

## Team Members

#### Team P
<ul>
	<li>Karan Bhanot (bhanok) - Team Leader</li> 
	<li>Tim Budding (buddit)</li>
	<li>Sen Francis (francs2)</li>
	<li>Zachary Koo (kooz2)</li>
</ul>

#### Team G
<ul>
	<li>Neha Deshpande (deshpn2)</li> 
	<li>Bowen Gong (gongb)</li>
	<li>Callum Hauber (haubec2)</li>
	<li>Justin Mai (maij)</li>
	<li>Matthew Scanlon (scanlm3)</li>
</ul>
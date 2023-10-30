Each line in ip2asn is a tab-separated list of values representing a single watch of a video.

The structure of the lines is constant, and every column is a data field. The relevant columns are

Column
Description
1
Start time of the transaction
2
Start time in seconds since Epoch
3
Duration - download time in millisecond
6
Site name of the video download
11
Video length in bytes
41
Subnet - a /24 mask of the client IP address (masked due to privacy regulations)


You are requested to write a program that analyzes metrics based on this file. The required metrics are total volume and average bandwidth, per site name.
Total volume - how many bytes where downloaded from this site
Average bandwidth - a transaction bandwidth is measured in bits/sec. Get the average bandwidth of all transactions from this site.
Now, given mapping of asn to subnet, calculate the ASN based on the Subnet field, and collect all ASNs each site delivered to.

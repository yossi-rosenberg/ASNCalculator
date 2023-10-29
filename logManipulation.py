import csv
import sitesData
import networkUtils
import fileUtils

def sites_bytes_and_bandwith():
    with open('resources/interview_mdl.log') as fd:
        sites_dictionary = {}
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            if not row[5] in sites_dictionary.keys():
                sites_dictionary[row[5]] = sitesData.SiteData(row[5] , int(row[10]) , int(row[2]))
            else:
                sites_dictionary[row[5]].add_bytes_to_site(int(row[10]))
        for key in sites_dictionary:
            print("site: " + str(sites_dictionary[key].site_downloaded_bytes) + " total bytes dowloaded")
            print("site: " + str(sites_dictionary[key].get_bandwith()) + " average bandwith")

def collect_asn():
    with open('resources/interview_mdl.log') as fd:
        sites_dictionary = {}
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            if row[40].rsplit("/").__getitem__(1) == '24':
                #print(networkUtils.mask_to_long(row[40].rsplit("/").__getitem__(0)))
                curr_asn = fileUtils.get_asn(networkUtils.mask_to_int(row[40].rsplit("/").__getitem__(0)))
                if not row[5] in sites_dictionary.keys():
                    sites_dictionary[row[5]] = {curr_asn}
                else:
                    sites_dictionary[row[5]].add(curr_asn)
        print(sites_dictionary)



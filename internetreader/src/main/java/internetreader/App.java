package internetreader;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;


import org.jsoup.Jsoup; 
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


public class App 
{
    public static void main( String[] args ) throws IOException {
        System.out.println("Major/Minor Puller");
        Document document = new Document("");

        String url = "https://catalog.lsu.edu/content.php?catoid=27&navoid=2375";
        Document catalogPage = Jsoup.connect(url).get();

        Element bigBox = catalogPage.getElementsByClass("block_content").first();

        Elements majorListings = bigBox.getElementsByTag("strong");

        for (int i = majorListings.size() - 1; i > 0; i--) {
            if (!(majorListings.get(i).html().equals("Major"))) {
                System.out.println("Removed " + majorListings.get(i).html());
                majorListings.remove(i);
            } else {
                System.out.println("Passed " + majorListings.get(i).html());
            }
        }

        Elements majorLinks;
        Elements links = new Elements();

        System.out.println("Going through listings");
        for (Element listing : majorListings) {
            //System.out.println(listing.html());
            System.out.println(listing.parent().html());
            Element programList = listing.parent().nextElementSibling();
            if (programList != null) {
                //System.out.println(programList.html());
                Elements listElements = programList.getElementsByTag("a");
                for (Element listElement : listElements) {
                    links.add(listElement);
                }
            }
        }

        Element majorRoot = document.createElement("Majors");
        document.appendChild(majorRoot);

        for (Element link : links) {
            String majorName = link.html();
            majorName.replace("&", "and");
            if(majorName.length() > 0 && majorName.charAt(0) != '<' && majorName != "Back to Top") {
                //System.out.println(majorName);
                Element major = document.createElement("Major");

                Element name = document.createElement("Name");
                name.html(majorName);
                major.appendChild(name);

                Element page = document.createElement("Link");
                String ur = link.attr("href");
                page.html("https://catalog.lsu.edu/" + ur);
                major.appendChild(page);

                majorRoot.appendChild(major);

            }
        }

        Document.OutputSettings docSetting = new Document.OutputSettings();
        docSetting.prettyPrint(true);
        docSetting.indentAmount(4);
        docSetting.outline(true);
        docSetting.syntax(Document.OutputSettings.Syntax.xml);
        document = document.outputSettings(docSetting);
        document.parser();
        BufferedWriter fw = new BufferedWriter(new FileWriter("majors.xml"));
        fw.write(document.toString());
        fw.close();

    }
    

}

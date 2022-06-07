import java.net.URL;
import java.net.URLConnection;

public class Remote extends Project {
    private String sURL;
    private String separator;
    private String data;

    public Remote(String author, String projectName, String separator) {
        super(author, projectName, null);
        this.sURL = "https://api.github.com/repos/" + author + "/" + projectName + "/releases/latest";
        this.separator = separator;

        // Get the latest Release JSON from the remote repository GitHub API
        this.data = "";
        // Use data to get tag_name field
        Version version = new Version("0.0.0", separator);
        // Update version in parent class
        this.setVersion(version);
    }

    public void refresh() {
        // CHANGE THIS TO USE A CUSTOM REQUEST FOR THE JSON
        try {
            URL url = new URL(this.sURL);
            URLConnection conn = url.openConnection();
            conn.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11");
            conn.connect();
            this.data = conn.getInputStream().toString();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public String getData() {
        return this.data;
    }
}
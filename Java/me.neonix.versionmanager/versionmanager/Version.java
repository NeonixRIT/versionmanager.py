import java.util.LinkedList;

public class Version implements Comparable<Version> {
    private LinkedList<String> versionList;
    private String version;

    public Version(String version, String separator) {
        this.version = version;
        this.versionList = new LinkedList<String>();
        for (String verStr : this.version.split(separator)) {
            versionList.add(verStr);
        }
    }

    public Version(String version) {
        this(version, ".");
    }

    @Override
    public String toString() {
        return this.version;
    }

    @Override
    public int compareTo(Version other) {
        int i = 0;
        while (i < this.versionList.size() && i < other.versionList.size()) {
            int thisVer = Integer.parseInt(this.versionList.get(i));
            int otherVer = Integer.parseInt(other.versionList.get(i));
            if (thisVer < otherVer) {
                return -1;
            } else if (thisVer > otherVer) {
                return 1;
            }
            i++;
        }
        return 0;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Version) {
            return this.compareTo((Version) obj) == 0;
        }
        return false;
    }
}

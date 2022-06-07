import java.util.HashSet;

public class VersionManager {
    private String author;
    private String projectName;
    private String separator;

    private Local local;
    private Remote remote;

    private HashSet<String> observers;

    public VersionManager(String author, String projectName, String version, String separator) {
        this.author = author;
        this.projectName = projectName;
        this.separator = separator;

        this.local = new Local(author, projectName, version, separator);
        this.remote = null;

        this.observers = new HashSet<>();
    }

    private void notifyObservers(HashSet<String> observers) {
        for (String observer : observers) {
            //observer.notify();
        }
    }

    public void registerObserver(String observer) {
        this.observers.add(observer);
    }

    public Status checkStatus() {
        Status status = null;

        if (this.remote == null) {
            this.remote = new Remote(this.author, this.projectName, this.separator);
        } else {
            this.remote.refresh();
        }

        if (this.local.getVersion().compareTo(this.remote.getVersion()) == 0) {
            status = Status.CURRENT;
        } else if (this.local.getVersion().compareTo(this.remote.getVersion()) < 0) {
            status = Status.OUTDATED;
        } else {
            status = Status.DEV;
        }
        this.notifyObservers(this.observers);
        return status;
    }
}
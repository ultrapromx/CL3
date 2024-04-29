import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Hotel extends Remote {
    String bookRoom(String guestName) throws RemoteException;
    String cancelBooking(String guestName) throws RemoteException;
}
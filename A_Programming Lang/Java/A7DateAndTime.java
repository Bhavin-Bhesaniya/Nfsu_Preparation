import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Locale;

public class A7DateAndTime {

  public static void main(String[] args) {

    // Print currentDate and time
    Date currentDate = new Date();
    System.out.println(currentDate.toString());

    // Print local machine date and time
    LocalDateTime myobj = LocalDateTime.now();
    System.out.println(myobj);

    // Format date and time
    DateTimeFormatter formobj = DateTimeFormatter.ofPattern("E,dd-MM-yyyy HH:mm:ss");
    String formatdt = myobj.format(formobj);
    System.out.println(formatdt);


    // Calendar
    String month[] = { "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" };

    // Store AM or PM
    String amPm[] = { "AM", "PM" };

    /* Creating object of GregorianCalendar class using default constructor */
    GregorianCalendar gcal = new GregorianCalendar();

    // GregorianCalendar gcal = new GregorianCalendar(2018, 3, 30); Passing year,
    // month, DayOfMonth, (hourOfDay,MINUTE,second,timezone,locale);

    // displaying date, time, time zone and locale
    System.out.print("Date: "
        + month[gcal.get(Calendar.MONTH)] + " "
        + gcal.get(Calendar.DATE) + ", "
        + gcal.get(Calendar.YEAR) + "\n"
        + "Time: "
        + gcal.get(Calendar.HOUR) + ":"
        + gcal.get(Calendar.MINUTE) + ":"
        + gcal.get(Calendar.SECOND) + " "
        + amPm[gcal.get(Calendar.AM_PM)] + "\n"
        + "Time Zone: " + gcal.getTimeZone().getDisplayName()
        + "\n"
        + "Locale: "
        + Locale.getDefault().getDisplayName());
  }
}
// delete the following sample code before you insert your code
// copy&paste your java code here
import java.sql.*;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import java.io.*;

public class memory {
    public static void main (String args [])
            throws SQLException, IOException {
        try
        {
            // Connect to the database
            Class.forName ("com.mysql.cj.jdbc.Driver");
            String host = "flora.hufs.ac.kr:3306/";
            String db= "s201901208db";
            String user = "s201901208";
            String password = getPassword();
            Connection con = DriverManager.getConnection("jdbc:mysql://" + host + db + "?useSSL=false&serverTimezone=Asia/Seoul", user, password);

            // Perform query using PreparedStatement
            // by providing SSN at run times
            String query ="with recursive Find_ssn AS ("+
                    "select e1.ssn,e1.superssn,0 as level "+
                    "from EMPLOYEE e1 "+
                    "where e1.ssn = ? " +
                    "union all" +
                    "select e.ssn , e.superssn ,fs.level+1 " +
                    "from EMPLOYEE e " +
                    "join Find_ssn fs ON e.superssn = fs.ssn " +
                    ") " +
                    "select ssn,level from Find_ssn order by level";
            PreparedStatement pstmt = con.prepareStatement(query);
            String ssn = readEntry("Enter a Social Security Number: ");
            pstmt.clearParameters();
            pstmt.setString(1,ssn);
            ResultSet rset = pstmt.executeQuery();

            // Process the ResultSet
            if (rset.next ()) {
                while (rset.next ()) {
                    String _ssn = rset.getString(1);
                    int level = rset.getInt(2);
                    System.out.println(_ssn + "\t" + level);
                }
                System.out.println("END OF LIST");
            }
            else {
                System.out.println("No Employees whose ssn is " + ssn);
            }

            // Close objects
            rset.close();
            pstmt.close();
            con.close();
        }
        catch (SQLException ex)
        {
            System.out.println("SQLException" + ex);
        }
        catch (Exception ex)
        {
            System.out.println("Exception:" + ex);
        }
    }

    private static String getPassword() {
        final String password, message = "Enter password";
        if(System.console() == null)
        {
            final JPasswordField pf = new JPasswordField();
            password = JOptionPane.showConfirmDialog(null, pf, message,
                    JOptionPane.OK_CANCEL_OPTION,
                    JOptionPane.QUESTION_MESSAGE ) == JOptionPane.OK_OPTION ?
                    new String(pf.getPassword()) : "";
        }
        else
            password = new String(System.console().readPassword("%s> ", message ));

        return password;
    }

    // ReadEntry function -- to read input string
    private static String readEntry(String prompt) {
        try {
            StringBuffer buffer = new StringBuffer();
            System.out.print(prompt);
            System.out.flush();
            int c = System.in.read();
            while (c != '\n' && c != -1) {
                buffer.append((char)c);
                c = System.in.read();
            }
            return buffer.toString().trim();
        } catch (IOException e) {
            return "";
        }
    }
}
// delete the following sample code before you insert your code
// copy&paste your java code here
import java.sql.*;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import java.io.*;

public class Main {
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
            Statement stmt = con.createStatement();
            stmt.execute("create temporary table if not exists tempssn (ssn CHAR(9), superssn CHAR(9), level INT) ENGINE = MEMORY");

            String query =
                    "select *" +
                    "from tempssn ts " +
                    "union all " +
                    "select e.ssn, e.superssn, ts.level + 1 " +
                    "from EMPLOYEE e " +
                    "join tempssn ts on e.superssn = ts.ssn " +
                    "where e.ssn = ?";

            String outputQuery = "select ssn, superssn, level from tempssn order by level";

            PreparedStatement pstmt = con.prepareStatement(query);
            String ssn = readEntry("Enter a Social Security Number: ");
            pstmt.clearParameters();
            pstmt.setString(1, ssn);
            ResultSet rset = pstmt.executeQuery();

            // Process the ResultSet
            if (rset.next()) {
                while (rset.next()) {
                    do {
                        pstmt.clearParameters();
                        pstmt.setString(1, ssn);
                        rset = pstmt.executeQuery();

                        ssn = rset.getString(1);
                        int level = rset.getInt(3);
                        pstmt.setString(1, ssn);
                    } while (rset.next());
                }

                System.out.println("END OF LIST");
            } else {
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
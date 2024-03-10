
import java.sql.*;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import java.io.*;

public class memory {
    public static void main(String args[]) throws SQLException, IOException {
        try {
            // Connect to the database
            Class.forName("com.mysql.cj.jdbc.Driver");
            String host = "flora.hufs.ac.kr:3306/";
            String db = "s201901208db";
            String user = "s201901208";
            String password = getPassword();
            Connection con = DriverManager.getConnection("jdbc:mysql://" + host + db + "?useSSL=false&serverTimezone=Asia/Seoul", user, password);

            // Create temporary table if not exists
            Statement stmt = con.createStatement();
            stmt.execute("CREATE TEMPORARY TABLE IF NOT EXISTS tempssn (ssn CHAR(9), superssn CHAR(9), level INT) ENGINE=MEMORY");

            // Insert the root employee into tempssn
            String rootSSN = readEntry("Enter a ssn: ");
            PreparedStatement initialStatement = con.prepareStatement("INSERT INTO tempssn (ssn, superssn, level) VALUES (?, NULL, 0)");
            initialStatement.setString(1, rootSSN);
            initialStatement.executeUpdate();

            String updateQuery =
                    "SELECT e.ssn, e.superssn, ts.level + 1 " +
                            "FROM EMPLOYEE e " +
                            "JOIN tempssn ts ON e.superssn = ts.ssn";

            int previousResultSetSize = 0;

            while (true) {
                try (PreparedStatement Ustmt = con.prepareStatement(updateQuery)) {
                    ResultSet Uset = Ustmt.executeQuery();
                    int currentResultSetSize = 0;

                    while (Uset.next()) {
                        currentResultSetSize++;

                        String _ssn = Uset.getString(1);
                        String _superssn = Uset.getString(2);
                        int _level = Uset.getInt(3);

                        if (!recordExists(con, _ssn, _superssn, _level)) {
                            stmt.execute("INSERT INTO tempssn (ssn, superssn, level) VALUES ('" + _ssn + "','" + _superssn + "'," + _level + ")");
                        }

                    }

                    if (currentResultSetSize == previousResultSetSize) {
                        break;
                    }

                    previousResultSetSize = currentResultSetSize;
                }
            }

            String outputQuery = "SELECT ssn, superssn, level FROM tempssn WHERE level > 0 ORDER BY level";
            ResultSet outputResult = stmt.executeQuery(outputQuery);

            while (outputResult.next()) {
                String ssnResult = outputResult.getString("ssn");
                int levelResult = outputResult.getInt("level");
                System.out.println(ssnResult + "\t" + levelResult);
            }
            System.out.println("END OF LIST");

            outputResult.close();
            initialStatement.close();
            stmt.close();
            con.close();
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    private static boolean recordExists(Connection con, String ssn, String superssn, int level) throws SQLException {
        String query = "SELECT COUNT(*) FROM tempssn WHERE ssn = ? AND superssn = ? AND level = ?";
        try (PreparedStatement stmt = con.prepareStatement(query)) {
            stmt.setString(1, ssn);
            stmt.setString(2, superssn);
            stmt.setInt(3, level);
            ResultSet resultSet = stmt.executeQuery();
            resultSet.next();
            int count = resultSet.getInt(1);
            return count > 0;
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
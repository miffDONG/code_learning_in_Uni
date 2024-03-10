import java.sql.*;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String args[]) throws SQLException {
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

            // PlusQuery to find direct and indirect subordinates
            String UpdateQuery =
                    "SELECT e.ssn, e.superssn, ts.level + 1 " +
                            "FROM EMPLOYEE e " +
                            "JOIN tempssn ts ON e.superssn = ts.ssn " +
                            "WHERE e.superssn = ?";

            // Initialize with the root employee
            String rootSSN = readEntry("Enter the root Social Security Number: ");
            List<Employee> resultList = new ArrayList<>();
            resultList.add(new Employee(rootSSN, null, 0));


            // Loop to find all direct and indirect subordinates
            try (PreparedStatement updateStatement = con.prepareStatement(UpdateQuery)) {
                System.out.println("입장");
                for (Employee employee : resultList) {
                    updateStatement.setString(1, employee.getSsn());
                    try (ResultSet resultSet = updateStatement.executeQuery()) {
                        while (resultSet.next()) {
                            System.out.println(resultSet);
                            String ssn = resultSet.getString("ssn");
                            String superssn = resultSet.getString("superssn");
                            int level = resultSet.getInt("level");
                            resultList.add(new Employee(ssn, superssn, level));
                        }
                    }
                }
            }

            // Insert resultList into tempssn
            try (PreparedStatement insertStatement = con.prepareStatement("INSERT INTO tempssn (ssn, superssn, level) VALUES (?, ?, ?)")) {
                for (Employee employee : resultList) {
                    insertStatement.setString(1, employee.getSsn());
                    insertStatement.setString(2, employee.getSuperssn());
                    insertStatement.setInt(3, employee.getLevel());
                    insertStatement.executeUpdate();
                }
            }

            // Display the results from tempssn
            try (ResultSet outputResult = stmt.executeQuery("SELECT * FROM tempssn")) {
                while (outputResult.next()) {
                    String ssn = outputResult.getString("ssn");
                    String superssn = outputResult.getString("superssn");
                    int level = outputResult.getInt("level");
                    System.out.println(ssn + "\t" + superssn + "\t" + level);
                }
            }

            // Close objects
            stmt.close();
            con.close();
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }


    private static String getPassword() {
        final String password, message = "Enter password";
        if (System.console() == null) {
            final JPasswordField pf = new JPasswordField();
            password = JOptionPane.showConfirmDialog(null, pf, message,
                    JOptionPane.OK_CANCEL_OPTION,
                    JOptionPane.QUESTION_MESSAGE) == JOptionPane.OK_OPTION ?
                    new String(pf.getPassword()) : "";
        } else
            password = new String(System.console().readPassword("%s> ", message));

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
                buffer.append((char) c);
                c = System.in.read();
            }
            return buffer.toString().trim();
        } catch (IOException e) {
            return "";
        }
    }

    static class Employee {
        private String ssn;
        private String superssn;
        private int level;

        public Employee(String ssn, String superssn, int level) {
            this.ssn = ssn;
            this.superssn = superssn;
            this.level = level;
        }

        public String getSsn() {
            return ssn;
        }

        public String getSuperssn() {
            return superssn;
        }

        public int getLevel() {
            return level;
        }
    }
}

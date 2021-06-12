import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server };"
                      "Server=info430group9.database.windows.net;"
                      "Database=INFO430_GROUP_PROJECT;"
                      "UID = info430group9;"
                      "PWD = group91234!;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM INFO430_GROUP_PROJECT]')
for row in cursor:
    print('row = %r' % (row,))


# <?php
# $serverName = "info430group9.database.windows.net";
# $uid = "info430group9";
# $pwd = "group91234!";
# $databaseName = "INFO430_GROUP_PROJECT";
# $connectionInfo = array( "UID"=>$uid,
#                          "PWD"=>$pwd,
#                          "Database"=>$databaseName);
# /* Connect using SQL Server Authentication. */
# $conn = sqlsrv_connect( $serverName, $connectionInfo);
# $tsql = "SELECT * FROM challenges";
# /* Execute the query. */
# $stmt = sqlsrv_query( $conn, $tsql);
# if ( $stmt )
# {
#      echo "Statement executed.<br>\n";
# }
# else
# {
#      echo "Error in statement execution.\n";
#      die( print_r( sqlsrv_errors(), true));
# }
# /* Iterate through the result set printing a row of data upon each iteration.*/
# while( $row = sqlsrv_fetch_array( $stmt, SQLSRV_FETCH_NUMERIC))
# {
#      echo "Col1: ".$row[0]."\n";
#      echo "Col2: ".$row[1]."\n";
#      echo "Col3: ".$row[2]."<br>\n";
#      echo "-----------------<br>\n";
# }
# /* Free statement and connection resources. */
# sqlsrv_free_stmt( $stmt);
# sqlsrv_close( $conn);
# ?>





# 1:11
# import pyodbc
# cnxn = pyodbc.connect("Driver={SQL Server };"
#                       "Server=info430group9.database.windows.net;"
#                       "Database=INFO430_GROUP_PROJECT;"
#                       "UID = info430group9;"
#                       "PWD = group91234!;"
#                       "Trusted_Connection=yes;")
# cursor = cnxn.cursor()
# cursor.execute('SELECT * FROM INFO430_GROUP_PROJECT]')
# for row in cursor:

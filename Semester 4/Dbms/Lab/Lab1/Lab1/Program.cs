using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
using System.Data;
//SqlConnection, SqlCommand, SqlDataReader, SqlDataAdapter
//DataSet
//SqlCommand = ExecuteScalar, ExecuteNonQuery
//
namespace Lab1
{
    class Program
    {
        static void Main(string[] args)
        {
            SqlConnection dbCon = new SqlConnection("Data Source = DESKTOP-FRG6FQT;  Initial Catalog = Modelut; Integrated Security = SSPI");
            dbCon.Open();
            Console.WriteLine("ok");
            dbCon.Close();

            /*
            DataSet ds = new DataSet();
            SqlDataAdapter da = new SqlDataAdapter("select * from T", dbCon);
            da.Fill(ds, "T");
            //foreach (DataRow dr in ds.Tables["T"].Rows)
            //Console.WriteLine("{0}\t{1}", dr["ID"], dr["ColA"]);
            SqlCommandBuilder cb = new SqlCommandBuilder(da);

            DataRow dr = ds.Tables["T"].NewRow();
            dr["id"] = 5486;
            dr["Cola"] = "ddd";
            ds.Tables["T"].Rows.Add(dr);

            da.Update(ds, "T");
            
            string sql = "select * from T";
            SqlCommand cmd = new SqlCommand(sql, dbCon);
            dbCon.Open();
            Console.WriteLine((Int32)cmd.ExecuteScalar());
            */

            string sql = "select * from T";
            SqlCommand cmd1 = new SqlCommand(sql, dbCon);
            dbCon.Open();
            Console.WriteLine((cmd1.ExecuteNonQuery()));
            Console.ReadLine();
        }

    }
}

public class SuccessActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_success);

        TextView welcomeText = findViewById(R.id.welcome);
        welcomeText.setText("Login Successful!");
    }
}

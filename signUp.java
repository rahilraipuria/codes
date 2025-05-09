public class SignUpActivity extends AppCompatActivity {
    EditText etUsername, etPassword;
    Button btnSignUp;
    public static String savedUsername = "", savedPassword = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);

        etUsername = findViewById(R.id.username);
        etPassword = findViewById(R.id.password);
        btnSignUp = findViewById(R.id.signup);

        btnSignUp.setOnClickListener(v -> {
            String username = etUsername.getText().toString();
            String password = etPassword.getText().toString();

            if (username.isEmpty() || password.isEmpty()) {
                Toast.makeText(this, "Fields cannot be empty", Toast.LENGTH_SHORT).show();
            } else {
                savedUsername = username;
                savedPassword = password;
                Toast.makeText(this, "Sign Up Successful", Toast.LENGTH_SHORT).show();
                startActivity(new Intent(this, SignInActivity.class));
                finish();
            }
        });
    }
}
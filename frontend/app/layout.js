import "./globals.css";

export const metadata = {
  title: "Azure OpenAI Chat",
  description: "FastAPI + Azure OpenAI chat frontend"
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div className="background" aria-hidden="true" />
        <main className="page">{children}</main>
      </body>
    </html>
  );
}

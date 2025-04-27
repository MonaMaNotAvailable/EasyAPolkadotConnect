import { Link } from 'react-router-dom';
import styles from './styles/navbar.module.css';

const Navbar = () => {
  return (
    <header className={styles.navbar}>
      <div className={styles.navContent}>
        <Link to="/" className={styles.brand}>
          <span className={styles.brandPrimary}>EasyA Polkadot </span>
          <span className={styles.brandSecondary}>Coffee Chat</span>
        </Link>
        <nav className={styles.navMenu}>
          <Link to="/" className={styles.navItem}>Home</Link>
          <Link to="/browse" className={styles.navItem}>Browse</Link>
          <Link to="/profile" className={styles.navItem}>Profile</Link>
        </nav>
      </div>
    </header>
  );
};

export default Navbar;